import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00065, -0.03518).lineTo(-0.02285, -0.03518).lineTo(-0.02285, -0.0065).lineTo(-0.00065, -0.0065).lineTo(-0.00065, -0.03518).close()
solid=wp_sketch0.add(loop0).extrude(0.056955166196201605)
