import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00302, -0.02708).lineTo(0.00302, -0.02929).lineTo(0.0316, -0.02981).lineTo(0.0316, -0.02745).lineTo(0.00302, -0.02708).close()
solid=wp_sketch0.add(loop0).extrude(0.06743045001093274)
