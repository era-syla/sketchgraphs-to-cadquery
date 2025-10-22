import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00844, 0.02683).lineTo(-0.02047, 0.02683).lineTo(-0.02047, 0.03302).lineTo(0.00844, 0.03302).lineTo(0.00844, 0.02683).close()
solid=wp_sketch0.add(loop0).extrude(-0.0012797146438524429)
