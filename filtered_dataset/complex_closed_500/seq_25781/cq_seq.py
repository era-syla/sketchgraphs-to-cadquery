import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.07483).lineTo(0.07923, 0.07483).lineTo(0.07923, -0.11017).lineTo(0.0, -0.11017).lineTo(0.0, 0.07483).close()
solid=wp_sketch0.add(loop0).extrude(0.2139228259525896)
