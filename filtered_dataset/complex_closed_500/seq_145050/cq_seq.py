import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.03469).lineTo(-0.01458, 0.03469).lineTo(-0.01458, -0.05854).lineTo(0.0, -0.05854).lineTo(0.0, -0.04308).lineTo(0.0, 0.03469).close()
solid=wp_sketch0.add(loop0).extrude(-0.006384598137695735)
