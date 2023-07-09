function toggle(section){
    all_nav_links = document.getElementsByClassName('nav-link');
    for (let i=0;i<all_nav_links.length;i++){
        all_nav_links[i].classList.remove('active')
    }
    
    all_sections = document.getElementsByClassName('sections');
    for (let i=0;i<all_sections.length;i++){
        all_sections[i].style.display = "none"
    }
    document.getElementById(section).style.display = "block"
    document.getElementById(section+"_nav").classList.add('active')
    // if(section === 'candidate'){
    //     all_nav_links = document.getElementsByClassName('nav-link');
    //     for (let i=0;i<all_nav_links.length;i++){
    //         all_nav_links[i]
    //     }

    //     document.getElementById('voter_section').style.display = 'none'
    //     document.getElementById('candidate_section').style.display = 'block'
    //     document.getElementById('candidate_nav').classList.add('active')
    //     document.getElementById('voter_nav').classList.remove('active')
    // }
    // else{
    //     document.getElementById('voter_section').style.display = 'block'
    //     document.getElementById('candidate_section').style.display = 'none'
    //     document.getElementById('voter_nav').classList.add('active')
    //     document.getElementById('candidate_nav').classList.remove('active')
    // }

}