function toggle(section){
    if(section === 'candidate'){
        document.getElementById('voter_section').style.display = 'none'
        document.getElementById('candidate_section').style.display = 'block'
        document.getElementById('candidate_nav').classList.add('active')
        document.getElementById('voter_nav').classList.remove('active')
    }
    else{
        document.getElementById('voter_section').style.display = 'block'
        document.getElementById('candidate_section').style.display = 'none'
        document.getElementById('voter_nav').classList.add('active')
        document.getElementById('candidate_nav').classList.remove('active')
    }

}