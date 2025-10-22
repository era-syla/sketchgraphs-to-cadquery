import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.00123).lineTo(0.32107, 0.00123).lineTo(0.32107, -0.02991).lineTo(0.0, -0.02991).lineTo(0.0, 0.00123).close()
solid=wp_sketch0.add(loop0).extrude(-0.01138690546545981)
