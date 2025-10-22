import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.004, -0.00327).lineTo(-0.004, -0.00327).lineTo(-0.004, -0.00831).lineTo(0.004, -0.00831).lineTo(0.004, -0.00327).close()
solid=wp_sketch0.add(loop0).extrude(0.012699466978664567)
