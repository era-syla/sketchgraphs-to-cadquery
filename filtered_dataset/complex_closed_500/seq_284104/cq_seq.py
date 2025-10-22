import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00549, -0.00771).lineTo(0.00907, 0.00269).lineTo(0.00549, 0.00771).lineTo(-0.00907, -0.00269).lineTo(-0.00549, -0.00771).close()
solid=wp_sketch0.add(loop0).extrude(0.03849312856851583)
