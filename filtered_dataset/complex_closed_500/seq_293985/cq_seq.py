import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.20345, 0.36285).lineTo(0.22885, 0.36285).lineTo(0.22885, 0.33745).lineTo(0.20345, 0.33745).lineTo(0.20345, 0.36285).close()
solid=wp_sketch0.add(loop0).extrude(0.027708732570250576)
