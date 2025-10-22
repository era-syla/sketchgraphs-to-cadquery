import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01677, -0.07287).lineTo(-0.03577, -0.04533).lineTo(-0.03577, 0.01613).lineTo(0.01065, 0.04622).lineTo(0.01677, -0.07287).close()
solid=wp_sketch0.add(loop0).extrude(-0.18165738127870354)
