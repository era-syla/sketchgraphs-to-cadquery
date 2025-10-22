import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04467, 0.08906).lineTo(0.05693, 0.08906).lineTo(0.05693, -0.08874).lineTo(-0.04467, -0.08874).lineTo(-0.04467, 0.08906).close()
solid=wp_sketch0.add(loop0).extrude(-0.3666367262396599)
