class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        n = len(people)
        person_skillset = [set(people[person]) for person in range(n)]
        for person1 in range(n):
            for person2 in range(person1+1, n):
                if person1 != person2 and person_skillset[person1] > person_skillset[person2]:
                    person_skillset[person2].clear()

        persons_have_the_skill = collections.defaultdict(set)
        for person, skills in enumerate(person_skillset):
            for skill in skills:
                persons_have_the_skill[skill].add(person)


        ans, skills_needed = [i for i in range(n)], set(req_skills)
        
        def bt(i, combo):
            nonlocal ans, skills_needed

            if len(combo) >= len(ans):
                return

            if not skills_needed:
                ans = list(combo)
                return

            if req_skills[i] not in skills_needed:
                return bt(i+1, combo)

            for person in persons_have_the_skill[ req_skills[i] ]:
                new_skills = person_skillset[person] & skills_needed
                
                combo.append(person)
                skills_needed -= new_skills
                bt(i+1, combo)
                combo.pop()
                skills_needed |= new_skills
        
        bt(0, [])
        return ans