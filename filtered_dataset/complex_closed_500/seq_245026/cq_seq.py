import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.37, -1.23).lineTo(-0.37, -1.23).lineTo(-0.37, -0.88).lineTo(0.37, -0.88).lineTo(0.37, -1.23).close()
solid=wp_sketch0.add(loop0).extrude(-0.20482270460706675)
