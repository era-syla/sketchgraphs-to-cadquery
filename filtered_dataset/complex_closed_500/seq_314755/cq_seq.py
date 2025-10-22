import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.2025, -0.25).lineTo(-0.2025, -0.25).lineTo(-0.2025, 0.25).lineTo(0.2025, 0.25).lineTo(0.2025, -0.25).close()
solid=wp_sketch0.add(loop0).extrude(0.9235758300420929)
