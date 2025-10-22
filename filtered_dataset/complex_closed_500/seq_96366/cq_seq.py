import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.27).lineTo(-0.01, -0.27).lineTo(-0.01, -0.28469).lineTo(0.0, -0.28469).lineTo(0.0, -0.27).close()
solid=wp_sketch0.add(loop0).extrude(-0.040777487046177015)
