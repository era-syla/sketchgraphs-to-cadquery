import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.6712, 0.92075).lineTo(-0.2432, 0.92075).lineTo(-0.2432, 2.13995).lineTo(0.6712, 2.13995).lineTo(0.6712, 0.92075).close()
solid=wp_sketch0.add(loop0).extrude(2.599640578570677)
