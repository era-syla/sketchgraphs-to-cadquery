import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00837, -0.01041).lineTo(0.00452, -0.01041).lineTo(0.00452, -0.06576).lineTo(0.00837, -0.06576).lineTo(0.00837, -0.01041).close()
solid=wp_sketch0.add(loop0).extrude(0.08746939894670815)
