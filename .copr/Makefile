srpm:
	LATEST_TAG=$$(curl -s https://api.github.com/repos/SimoHypers/limusic/releases/latest | grep -o '"tag_name": *"[^"]*"' | cut -d'"' -f4); \
	VERSION=$$(echo $$LATEST_TAG | sed 's/^v//'); \
	mkdir -p /root/rpmbuild/SOURCES /root/rpmbuild/SPECS /root/rpmbuild/SRPMS; \
	cp limusic.spec /root/rpmbuild/SPECS/; \
	sed -i "s/%{limusic_version}/$$VERSION/g" /root/rpmbuild/SPECS/limusic.spec; \
	curl -L -o /root/rpmbuild/SOURCES/limusic-$${VERSION}-1.x86_64.rpm "https://github.com/SimoHypers/limusic/releases/download/v$${VERSION}/limusic-$${VERSION}-1.x86_64.rpm"; \
	rpmbuild -bs --define "_topdir /root/rpmbuild" /root/rpmbuild/SPECS/limusic.spec; \
	cp /root/rpmbuild/SRPMS/*.src.rpm $(outdir)/
