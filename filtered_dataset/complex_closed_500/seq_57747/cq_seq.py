import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0185, 0.0).lineTo(-0.0225, 0.0).lineTo(-0.0225, -0.0084).lineTo(-0.0185, -0.0047).lineTo(-0.0185, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0013076291224491134)
