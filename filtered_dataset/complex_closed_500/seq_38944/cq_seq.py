import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.025, -0.0).lineTo(0.025, -0.0).lineTo(0.025, -0.046).lineTo(-0.025, -0.046).lineTo(-0.025, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.13635602094520685)
