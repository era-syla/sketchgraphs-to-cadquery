import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0025, -0.003).lineTo(-0.0005, -0.001).lineTo(-0.0025, -0.003).lineTo(0.0025, -0.003).close()
solid=wp_sketch0.add(loop0).extrude(0.013191230031966664)
