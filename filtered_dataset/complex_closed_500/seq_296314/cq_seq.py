import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.25, 0.25).lineTo(-0.25, 0.25).lineTo(-0.25, -0.25).lineTo(0.25, -0.25).lineTo(0.25, 0.25).close()
solid=wp_sketch0.add(loop0).extrude(1.3774771187960022)
