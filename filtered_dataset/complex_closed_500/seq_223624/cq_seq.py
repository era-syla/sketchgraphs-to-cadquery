import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.025, 0.01).lineTo(-0.025, 0.01).lineTo(-0.025, -0.01).lineTo(0.025, -0.01).lineTo(0.025, 0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.11392524348717306)
