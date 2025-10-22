import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03, 0.01).lineTo(0.05, 0.01).lineTo(0.05, -0.01).lineTo(-0.03, -0.01).lineTo(-0.03, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.1489695166384066)
