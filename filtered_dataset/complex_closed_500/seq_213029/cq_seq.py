import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(2.63388, 0.49328).lineTo(2.82875, 0.49328).lineTo(2.82875, 2.67594).lineTo(2.63388, 2.67594).lineTo(2.63388, 0.49328).close()
solid=wp_sketch0.add(loop0).extrude(-1.823611377314979)
