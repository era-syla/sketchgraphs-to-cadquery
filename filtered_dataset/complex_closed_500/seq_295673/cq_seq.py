import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03221, -0.05067).lineTo(0.00579, -0.05067).lineTo(0.00579, -0.02167).lineTo(-0.03221, -0.02167).lineTo(-0.03221, -0.05067).close()
solid=wp_sketch0.add(loop0).extrude(0.06568339612300646)
