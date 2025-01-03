document.addEventListener('DOMContentLoaded', function() {
    const topicCards = document.querySelectorAll('.card-header');

    function getLightColor(index) {
        const hue = (index * 45) % 360;       
        const saturation = 70;                
        const lightness = 90;                
        return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
    }

    topicCards.forEach((card, index) => {
        const color = getLightColor(index);  
        card.style.backgroundColor = color;  
    });
});


let mybutton = document.getElementById("backToTop");

window.onscroll = function() {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    mybutton.style.display = "block";
    } else {
    mybutton.style.display = "none";
    }
};

mybutton.onclick = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};


document.querySelectorAll("#tutorial-content pre code").forEach(function (codeBlock) {
    let pre = codeBlock.parentElement;

    // Ensure <pre> is styled for relative positioning and horizontal scrolling
    pre.style.position = "relative";
    pre.style.overflowX = "auto"; // Allow horizontal scrolling if needed

    // Create the floating copy button
    let copyButton = document.createElement("button");
    copyButton.className = "copy-btn";
    copyButton.style.position = "absolute";
    copyButton.style.top = "10px";  // Adjust vertical position
    copyButton.style.right = "10px";  // Adjust horizontal position
    copyButton.style.background = "transparent";
    copyButton.style.border = "none";
    copyButton.style.cursor = "pointer";
    copyButton.style.color = "#6c757d";
    copyButton.style.fontSize = "14px";
    copyButton.innerHTML = `<i class="bi bi-clipboard"></i>`;
    copyButton.setAttribute("data-bs-toggle", "tooltip");
    copyButton.setAttribute("data-bs-placement", "top");
    copyButton.setAttribute("title", "Copy to clipboard");

    // Initialize the tooltip for this button
    new bootstrap.Tooltip(copyButton);

    // Copy functionality
    copyButton.addEventListener("click", function () {
        navigator.clipboard.writeText(codeBlock.innerText).then(() => {
            // Change tooltip to "Copied!" on success
            copyButton.setAttribute("data-bs-original-title", "Copied!");
            bootstrap.Tooltip.getInstance(copyButton).show();

            setTimeout(() => {
                copyButton.setAttribute("data-bs-original-title", "Copy to clipboard");
                bootstrap.Tooltip.getInstance(copyButton).hide();
            }, 2000);
        });
    });

    // Append copy button to <pre> block
    pre.appendChild(copyButton);

    // Ensure the copy button stays in the top-right corner when scrolling
    pre.addEventListener('scroll', function() {
        copyButton.style.right = (10 - pre.scrollLeft) + 'px';
    });
});




document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    const card = document.getElementById('sidebar-card');

    if (navbar && card) {
        const navbarHeight = navbar.offsetHeight;

        window.addEventListener('scroll', function() {
            const cardTop = card.getBoundingClientRect().top;

            if (cardTop <= navbarHeight) {
                card.style.position = 'absolute';
                card.style.top = `${navbarHeight}px`;
            } else {
                card.style.position = 'sticky';
                card.style.top = '0';
            }
        });
    }
});



// Function to toggle class based on screen size
function handleResponsiveClass() {
    const rowElement = document.querySelector('.equal-height-row');

    if (rowElement) {
        if (window.matchMedia('(max-width: 576px)').matches) {
            // Small screen: Remove the class
            rowElement.classList.remove('equal-height-row');
        } else {
            // Larger screen: Add the class back
            rowElement.classList.add('equal-height-row');
        }
    }
}

// Run on page load
handleResponsiveClass();

// Run on window resize
window.addEventListener('resize', handleResponsiveClass);

function addClassToTopStory2() {
    const smallScreenQuery = window.matchMedia("(max-width: 768px)");
    const topStory2Element = document.getElementById("topStory-2");

    if (smallScreenQuery.matches) {
        topStory2Element.classList.add("py-3");
    } else {
        topStory2Element.classList.remove("py-3");
    }
}

// Run on initial load
addClassToTopStory2();

// Listen for screen size changes
window.addEventListener("resize", addClassToTopStory2);

document.addEventListener('DOMContentLoaded', function() {
    var contentDiv = document.querySelector('#tutorial-content pre code');
    if(contentDiv) {
        contentDiv.innerText = "This is a very long line of code that should cause horizontal scrolling to ensure that the horizontal scrollbar appears within the pre element and not the entire page.";
    }
});




document.addEventListener('DOMContentLoaded', function() {
    // Handle dropdown menu for small screens
    var dropdownItems = document.querySelectorAll('.dropdown-item');
    var dropdownToggle = document.querySelector('.custom-dropdown-toggle');

    dropdownItems.forEach(function(item) {
      item.addEventListener('click', function(event) {
        event.preventDefault();
        var tabId = item.getAttribute('href');
        // Update the tab content
        var allTabs = document.querySelectorAll('.tab-pane');
        allTabs.forEach(function(tab) {
          tab.classList.remove('show', 'active');
        });
        var selectedTab = document.querySelector(tabId);
        if (selectedTab) {
          selectedTab.classList.add('show', 'active');
        }
        // Update dropdown label
        if (dropdownToggle) {
          dropdownToggle.textContent = item.textContent + ' ';
          var icon = document.createElement('i');
          icon.className = 'fas fa-chevron-down';
          dropdownToggle.appendChild(icon);
        }
      });
    });
  });
