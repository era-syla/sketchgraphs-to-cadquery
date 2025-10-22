import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.025, 0.0325).lineTo(0.025, 0.0325).lineTo(0.025, -0.0325).lineTo(-0.025, -0.0325).lineTo(-0.025, 0.0325).close()
solid=wp_sketch0.add(loop0).extrude(0.13965422634831232)
