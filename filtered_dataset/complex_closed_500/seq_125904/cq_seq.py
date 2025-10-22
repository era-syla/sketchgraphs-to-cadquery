import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04926, -0.00683).lineTo(-0.02831, -0.00683).lineTo(-0.02831, -0.00903).lineTo(-0.04926, -0.00903).lineTo(-0.04926, -0.00683).close()
solid=wp_sketch0.add(loop0).extrude(-0.05076219549087816)
