import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05895, -0.04073).lineTo(-0.03695, -0.04073).lineTo(-0.03695, -0.03196).lineTo(-0.05895, -0.03196).lineTo(-0.05895, -0.04073).close()
solid=wp_sketch0.add(loop0).extrude(0.06356526405032586)
