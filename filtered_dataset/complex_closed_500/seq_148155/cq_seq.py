import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.033, 0.028).lineTo(0.033, 0.028).lineTo(0.033, -0.028).lineTo(-0.033, -0.028).lineTo(-0.033, 0.028).close()
solid=wp_sketch0.add(loop0).extrude(-0.09904477300261036)
