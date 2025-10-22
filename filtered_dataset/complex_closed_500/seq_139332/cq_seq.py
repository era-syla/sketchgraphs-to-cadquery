import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01, 0.2).lineTo(-0.01, 0.2).lineTo(-0.01, 0.188).lineTo(0.01, 0.188).lineTo(0.01, 0.2).close()
solid=wp_sketch0.add(loop0).extrude(-0.05531458384527333)
