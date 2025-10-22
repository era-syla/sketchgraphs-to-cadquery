import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.9575, 0.42).lineTo(0.2625, 0.42).lineTo(0.2625, -0.4025).lineTo(-0.9575, -0.4025).lineTo(-0.9575, 0.42).close()
solid=wp_sketch0.add(loop0).extrude(-1.4869389708097902)
