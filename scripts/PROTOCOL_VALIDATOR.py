#!/usr/bin/env python3
"""
PROTOCOL_VALIDATOR.py
Validator for compliance with PROTOCOL_INVARIANTS.yaml
"""

import yaml
import json
import re
from pathlib import Path

class ProtocolValidator:
    def __init__(self, invariants_path="PROTOCOL/v1.0/PROTOCOL_INVARIANTS.yaml"):
        self.invariants = self.load_invariants(invariants_path)
        
    def load_invariants(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def validate_file(self, filepath):
        """Main validation function"""
        print(f"\n🔍 Validating: {filepath}")
        
        content = Path(filepath).read_text(encoding='utf-8')
        
        # 1. Check prohibited reading patterns
        if not self.check_reading_modes(content):
            return False
            
        # 2. Check temporal invariants
        if not self.check_temporal_invariants(content):
            return False
            
        # 3. Check for reification
        if not self.check_anti_reification(content):
            return False
            
        # 4. Check operations (for API_SPECIFICATION)
        if "API_SPECIFICATION" in filepath:
            if not self.check_operations(content):
                return False
                
        # 5. Check JSON-LD (for structured_data.jsonld)
        if filepath.endswith(".jsonld"):
            if not self.validate_jsonld(content):
                return False
                
        print("✅ File passes protocol validation")
        return True
    
    def check_reading_modes(self, content):
        """Check for prohibited reading modes"""
        prohibited = self.invariants['reading_mode']['prohibited_modes']
        
        danger_phrases = [
            "is defined as",
            "definition of",
            "entity with",
            "property of",
            "static description"
        ]
        
        for phrase in danger_phrases:
            if phrase in content.lower():
                print(f"❌ Found prohibited phrase: '{phrase}'")
                return False
        return True
    
    def check_temporal_invariants(self, content):
        """Check temporal invariants"""
        required_time = [
            "irreversible",
            "cannot return",
            "cannot be undone",
            "temporal"
        ]
        
        found = False
        for term in required_time:
            if term in content.lower():
                found = True
                break
                
        if not found:
            print("❌ Missing temporal irreversibility markers")
            return False
        return True
    
    def check_anti_reification(self, content):
        """Detect hidden reification"""
        noun_patterns = [
            r'\b(the|a|an) ([a-z]+) is\b',
            r'\b([A-Z][a-z]+) (?:has|contains|includes)\b'
        ]
        
        for pattern in noun_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                print(f"❌ Possible reification detected with pattern: {pattern}")
                return False
        return True
    
    def check_operations(self, content):
        """Check operations in API specification"""
        forbidden_ops = self.invariants['operational']['not_operations']
        
        for op in forbidden_ops:
            pattern = fr'\b{op}_[a-z]+\b'
            if re.search(pattern, content, re.IGNORECASE):
                print(f"❌ Found forbidden operation: {op}_*")
                return False
        return True
    
    def validate_jsonld(self, content):
        """Validate JSON-LD for process orientation"""
        try:
            data = json.loads(content)
            
            if '@graph' in data:
                for item in data['@graph']:
                    if '@type' in item:
                        type_value = item['@type']
                        if isinstance(type_value, str):
                            type_value = [type_value]
                        
                        allowed_types = ['process', 'Action', 'Event', 'constraint']
                        if not any(t in allowed_types for t in type_value):
                            print(f"❌ Invalid @type in JSON-LD: {type_value}")
                            return False
            return True
            
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            return False

if __name__ == "__main__":
    validator = ProtocolValidator()
    
    files_to_check = [
        "MACHINE_README.md",
        "QUICK_START_FOR_AI.yaml",
        "API_SPECIFICATION.yaml",
        "structured_data.jsonld"
    ]
    
    all_valid = True
    for file in files_to_check:
        if Path(file).exists():
            if not validator.validate_file(file):
                all_valid = False
        else:
            print(f"⚠ File not found: {file}")
    
    if all_valid:
        print("\n🎉 All files pass protocol validation!")
        print("Next: Run integration tests with actual AI parsers.")
    else:
        print("\n❌ Protocol validation failed. Review files.")
        exit(1)
