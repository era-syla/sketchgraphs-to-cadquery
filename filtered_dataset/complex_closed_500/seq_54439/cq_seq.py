import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1475, -0.7).lineTo(0.1025, -0.7).lineTo(0.1025, -0.605).lineTo(-0.1475, -0.605).lineTo(-0.1475, -0.7).close()
solid=wp_sketch0.add(loop0).extrude(0.04443515603993564)
