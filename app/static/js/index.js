function collapseAndExpand(requestQuery){
    document.querySelector(`${requestQuery} .header`).onclick = function(){
        document.querySelectorAll(`${requestQuery} .collapse-expand`).forEach(function(collapseExpand){
            if (!collapseExpand.style.display){
                collapseExpand.style.display = 'block';
            } else if (collapseExpand.style.display === 'none'){
                collapseExpand.style.display = 'block';
            } else {
                collapseExpand.style.display = 'none';
            }
        })

        return false;
    }
}

function listAllEvents(formQuery){
    // when click at the "Get API" button
    document.querySelector(`${formQuery} .get-api-button`).onclick = function(){
        this.form.onsubmit = () => {
            open('/api/v1/event/list', '_blank');

            return false;
        }
    }

    // when click at the "Send" button
    document.querySelector(`${formQuery} .send-button`).onclick = function(){
        this.form.onsubmit = () => {
            // initialize new request
            const xhr = new XMLHttpRequest();
            xhr.open('GET', '/event/list');
    
            // callback function for when requests completes
            xhr.onload = () => {
                // display status code
                if (xhr.status === 200){
                    document.querySelector(`${formQuery} .status-code`).innerHTML = '200 (Success)'
                } else {
                    document.querySelector(`${formQuery} .status-code`).innerHTML = `${xhr.status} (Failed)`
                };
    
                // modify <pre> tag for pretty json format
                document.querySelector(`${formQuery} pre`).innerHTML = xhr.responseText;           
            }
            xhr.send();
            return false;
        }
    }   

}

function createAnEvent(formQuery){
    document.querySelector(formQuery).onsubmit = () => {
        // get input body from user
        const responseBody = document.querySelector(`${formQuery} textarea`).value;

        // initialize new request
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/event');

        xhr.onload = () => {
            // display status code
            if (xhr.status === 200){
                document.querySelector(`${formQuery} .status-code`).innerHTML = '200 (Success)';
            } else {
                document.querySelector(`${formQuery} .status-code`).innerHTML = `${xhr.status} (Failed)`
            };

            // modify <pre> tag for pretty json format
            document.querySelector(`${formQuery} pre`).innerHTML = xhr.responseText;           
        }

        const data = new FormData();
        data.append('responseBody', responseBody);     
        xhr.send(data);

        return false;
    }
}

function showAnEvent(formQuery){
    
    
    

    // when click at the "Get API" button
    document.querySelector(`${formQuery} .get-api-button`).onclick = function(){
        this.form.onsubmit = () => {
            // get input id from user
            const eventID = document.querySelector(`${formQuery} input`).value;

            open(`/api/v1/event/${eventID}`, '_blank');
            return false;
        }
    }

    // when click at the "Send" button
    document.querySelector(`${formQuery} .send-button`).onclick = function(){
        this.form.onsubmit = () => {
            // get input id from user
            const eventID = document.querySelector(`${formQuery} input`).value;

            // initialize new request
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `/event/${eventID}`);

            xhr.onload = () => {
                // display status code
                if (xhr.status === 200){
                    document.querySelector(`${formQuery} .status-code`).innerHTML = '200 (Success)'
                } else {
                    document.querySelector(`${formQuery} .status-code`).innerHTML = `${xhr.status} (Failed)`
                };

                // modify <pre> tag for pretty json format
                document.querySelector(`${formQuery} pre`).innerHTML = xhr.responseText;         
            };

            xhr.send();
            return false
        }
    }

};

function addVotesToEvent(formQuery){
    document.querySelector(formQuery).onsubmit = () => {
        // get input id and request body from user
        const eventID = document.querySelector(`${formQuery} input`).value;
        const responseBody = document.querySelector(`${formQuery} textarea`).value;

        // initialize new request
        const xhr = new XMLHttpRequest();
        xhr.open('POST', `/event/${eventID}/vote`);

        xhr.onload = () => {
            // display status code
            if (xhr.status === 200){
                document.querySelector(`${formQuery} .status-code`).innerHTML = '200 (Success)'
            } else {
                document.querySelector(`${formQuery} .status-code`).innerHTML = `${xhr.status} (Failed)`
            };

            // modify <pre> tag for pretty json format
            document.querySelector(`${formQuery} pre`).innerHTML = xhr.responseText;
        }

        const data = new FormData();
        data.append('responseBody', responseBody);

        xhr.send(data);
        return false;
    }
};

function showResultsOfEvent(formQuery){
    
    // when click at the "Get API" button
    document.querySelector(`${formQuery} .get-api-button`).onclick = function(){
        this.form.onsubmit = () => {
            // get input id from user
            const eventID = document.querySelector(`${formQuery} input`).value;

            open(`/api/v1/event/${eventID}/results`, '_blank');
            return false;
        }
    }

    // when click at the "Send" button
    document.querySelector(`${formQuery} .send-button`).onclick = function(){
        this.form.onsubmit = () => {
            // get input id from user
            const eventID = document.querySelector(`${formQuery} input`).value;

            // initialize new request
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `event/${eventID}/results`);

            xhr.onload = () => {
                // display status code
                if (xhr.status === 200){
                    document.querySelector(`${formQuery} .status-code`).innerHTML = '200 (Success)';
                } else {
                    document.querySelector(`${formQuery} .status-code`).innerHTML = `${xhr.status} (Failed)`
                };

                // modify <pre> tag for pretty json format
                document.querySelector(`${formQuery} pre`).innerHTML = xhr.responseText;
            }

            xhr.send();
            return false;
        }
    }

};


document.addEventListener('DOMContentLoaded', (event) => {    
    event.preventDefault();

    const requestQueryList = ['#list-all-events', '#create-an-event', '#show-an-event', '#add-votes-to-event', '#show-results-of-event'];

    // placeholder for textarea 
    document.querySelector('#create-an-event textarea').placeholder = JSON.stringify(JSON.parse('{"name": "Jake\'s secret party","dates": ["2014-01-01", "2014-01-05", "2014-01-12"]}'), undefined, 4);

    document.querySelector('#add-votes-to-event textarea').placeholder = JSON.stringify(JSON.parse('{"name": "Dick", "votes": ["2014-01-01", "2014-01-05"]}'), undefined, 4);


    // event for collapse/expand of all requests
    requestQueryList.forEach((requestQuery) => {
        collapseAndExpand(requestQuery);
    });

    // ajax call to send API
    listAllEvents(formQuery='#list-all-events');
    createAnEvent(formQuery='#create-an-event')
    showAnEvent(formQuery='#show-an-event');
    addVotesToEvent(formQuery='#add-votes-to-event');
    showResultsOfEvent(formQuery='#show-results-of-event');
})


