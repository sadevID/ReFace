METADATA =\
{
	'name': 'ReFace',
	'description': 'Next generation face swapper and enhancer',
	'version': '1.3.1',
	'license': 'MIT',
	'author': 'SA DevLabs',
	'url': 'https://dev.samedia.biz.id'
}


def get(key : str) -> str:
	return METADATA[key]
