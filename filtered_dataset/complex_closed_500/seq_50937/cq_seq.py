import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00585, 0.00471).lineTo(0.00785, 0.00471).lineTo(0.00785, 0.00944).lineTo(-0.00585, 0.00944).lineTo(-0.00585, 0.00471).close()
solid=wp_sketch0.add(loop0).extrude(-0.022116448824225882)
