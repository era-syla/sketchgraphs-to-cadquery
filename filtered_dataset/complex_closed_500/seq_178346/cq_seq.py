import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.31834, 0.01).lineTo(0.31834, 0.01).lineTo(0.31834, -0.01).lineTo(-0.31834, -0.01).lineTo(-0.31834, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(1.3123757219100498)
