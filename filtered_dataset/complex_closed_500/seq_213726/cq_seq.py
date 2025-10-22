import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.001, 0.03777).lineTo(0.001, 0.03777).lineTo(0.001, 0.07777).lineTo(-0.001, 0.07777).lineTo(-0.001, 0.03777).close()
solid=wp_sketch0.add(loop0).extrude(-0.05053693119043781)
