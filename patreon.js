el = document.getElementById('__NEXT_DATA__');
text = el.innerText;
data = JSON.parse(text);
elements = data.props.pageProps.bootstrapEnvelope.pageBootstrap.post.included
imgs = elements.filter(x => x.attributes.hasOwnProperty('file_name') && x.attributes.hasOwnProperty('download_url'));

async function autoDownloadImage(url, filename) {
    const response = await fetch(url, { mode: 'cors' });
    const blob = await response.blob();
    const blobUrl = URL.createObjectURL(blob);
    attr = el.attributes;
    link = document.createElement('a');
    link.href = url;
    link.download = filename; 
    document.body.appendChild(link);
    setTimeout(() => {
        link.click();
        document.body.removeChild(link);
    }, 1000);
    URL.revokeObjectURL(blobUrl);
}

for (el of imgs){
    attr = el.attributes;
    autoDownloadImage(attr.download_url, attr.file_name);
}
