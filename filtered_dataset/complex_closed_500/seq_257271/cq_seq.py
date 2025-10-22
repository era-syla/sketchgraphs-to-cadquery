import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03358, -0.01343).lineTo(-0.02435, -0.01343).lineTo(-0.02435, -0.00143).lineTo(-0.03358, -0.00143).lineTo(-0.03358, -0.01343).close()
solid=wp_sketch0.add(loop0).extrude(0.018385469030303865)
