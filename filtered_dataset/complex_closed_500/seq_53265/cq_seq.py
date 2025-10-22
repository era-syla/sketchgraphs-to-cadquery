import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02, 0.19336).lineTo(0.07743, 0.1688).lineTo(0.07743, 0.1888).lineTo(-0.02073, 0.21336).lineTo(-0.02, 0.19336).close()
solid=wp_sketch0.add(loop0).extrude(0.06753206775627134)
