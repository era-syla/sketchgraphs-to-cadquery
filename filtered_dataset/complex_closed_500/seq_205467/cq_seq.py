import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.04647, 6.31745).lineTo(4.54647, 6.31745).lineTo(4.54647, 0.31745).lineTo(1.04647, 0.31745).lineTo(1.04647, 6.31745).close()
solid=wp_sketch0.add(loop0).extrude(14.368041516315298)
