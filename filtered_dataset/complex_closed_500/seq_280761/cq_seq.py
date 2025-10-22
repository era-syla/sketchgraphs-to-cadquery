import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03865, 0.06104).lineTo(-0.04469, 0.04811).lineTo(-0.04085, 0.05035).lineTo(-0.03734, 0.04871).lineTo(-0.03424, 0.05162).lineTo(-0.03865, 0.06104).close()
solid=wp_sketch0.add(loop0).extrude(-0.030026657232844083)
