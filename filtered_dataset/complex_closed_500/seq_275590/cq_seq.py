import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0055, 0.043).lineTo(-0.0055, 0.0).lineTo(0.01, 0.0).lineTo(0.01, 0.004).lineTo(-0.0, 0.004).lineTo(0.0, 0.023).lineTo(-0.0025, 0.023).lineTo(-0.0025, 0.043).lineTo(-0.0055, 0.043).close()
solid=wp_sketch0.add(loop0).extrude(0.06851881561874215)
