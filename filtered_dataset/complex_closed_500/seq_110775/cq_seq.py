import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.01219, 0.0).lineTo(0.01219, 0.0095).lineTo(-0.0, 0.0095).lineTo(0.0, 0.00292).lineTo(0.00686, 0.00292).lineTo(0.00686, -0.00292).lineTo(0.0, -0.00292).lineTo(0.0, -0.0095).lineTo(0.01219, -0.0095).lineTo(0.01219, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.04382024845013714)
