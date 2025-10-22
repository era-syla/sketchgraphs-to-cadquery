import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06619, 0.00592).lineTo(0.06529, 0.00856).lineTo(0.06979, 0.00498).lineTo(0.06619, 0.00592).close()
solid=wp_sketch0.add(loop0).extrude(-0.0038475793364754008)
