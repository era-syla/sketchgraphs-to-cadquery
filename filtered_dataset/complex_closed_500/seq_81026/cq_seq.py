import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01969, 0.00632).lineTo(-0.01896, 0.00757).lineTo(-0.02059, 0.00757).lineTo(-0.01969, 0.00632).close()
solid=wp_sketch0.add(loop0).extrude(-0.0017133531323779423)
