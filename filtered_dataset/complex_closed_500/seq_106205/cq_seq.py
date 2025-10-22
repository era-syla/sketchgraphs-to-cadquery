import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01392, 0.02322).lineTo(-0.00045, -0.02707).lineTo(0.01392, -0.02322).lineTo(0.00045, 0.02707).lineTo(-0.01392, 0.02322).close()
solid=wp_sketch0.add(loop0).extrude(0.004006093019115464)
