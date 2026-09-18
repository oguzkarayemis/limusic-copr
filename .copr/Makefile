# COPR bu dosyayı proje ayarlarında "Build SRPM with: make_srpm" seçilince,
# root yetkisiyle ve ağ erişimi açık bir mock chroot içinde çalıştırır.

srpm:
	# 1) Upstream Limusic reposundan en son release tag'ini çek (v0.7.3 gibi)
	LATEST_TAG=$$(curl -s https://api.github.com/repos/SimoHypers/limusic/releases/latest \
		| grep -o '"tag_name": *"[^"]*"' | cut -d'"' -f4); \
	VERSION=$$(echo $$LATEST_TAG | sed 's/^v//'); \
	echo "En son Limusic sürümü: $$VERSION"; \
	\
	mkdir -p /root/rpmbuild/SOURCES /root/rpmbuild/SPECS /root/rpmbuild/SRPMS; \
	cp limusic.spec /root/rpmbuild/SPECS/; \
	\
	# 2) Gerçek RPM'i indirip SOURCES'a koy (rpmbuild -bs bunu yerelde bekliyor)
	curl -L -o /root/rpmbuild/SOURCES/limusic-$${VERSION}-1.x86_64.rpm \
		"https://github.com/SimoHypers/limusic/releases/download/v$${VERSION}/limusic-$${VERSION}-1.x86_64.rpm"; \
	\
	# 3) SRPM'i üret
	rpmbuild -bs \
		--define "_topdir /root/rpmbuild" \
		--define "limusic_version $$VERSION" \
		/root/rpmbuild/SPECS/limusic.spec; \
	cp /root/rpmbuild/SRPMS/*.src.rpm "$$outdir/"
